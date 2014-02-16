define([
	'jquery',
	'underscore',
	'd3',
	'topojson',
], function ($, _, d3, topojson) {

	function translate(coords, dists) {
		return [coords[0] + dists[0], coords[1] + dists[1]];
	}

	function scale(coords, k) {
		return [coords[0] * k, coords[1] * k];
	}

	function polygon(d) {
		return "M" + d.join("L") + "Z";
	}

	function dangerLevelToColor(dangerLevel) {
		return d3.interpolateHsl('green', 'red')(dangerLevel / 100);
	}

	/**
	 * Makes a world map from given data
	 *
	 * @param  element    $el      jquery reference for container; replace this container's contents with the map
	 * @param  {Object}   options  Object containing options, none currently defined
	 *                    .clicked Callback for when a country is clicked, clicked(map, country, evt)
	 * @param  {Function} callback A function to be called when the mapping is done, callback(this, error);
	 */
	function Map($el, opts, callback) {
		var that = this;
		var error = null;

		this.width = $el.width(),
		this.height = 500; // TODO(zjn) not hardcode
		this.svg = d3.select($el.get(0)).append("svg")
			.attr("width", this.width)
			.attr("height", this.height);
		this.projection = d3.geo.equirectangular()
			.scale((this.width + 1) / 2 / Math.PI)
			.translate([this.width / 2, this.height / 1.8]);
		this.path = d3.geo.path()
			.projection(this.projection);

		d3.json("/static/app/world.topo.json", function(error, data) {
			//var subunits = that.svg.insert('g', ':first-child')
			var g = that.svg.append("g")
				.attr("id", "pointsLayer");
			var background = that.svg.insert('g')
				.attr('id', 'background')
				.attr('class', 'datamaps-subunits');
			var subunits = that.svg.insert('g')
				.attr('id', 'foreground')
				.attr('class', 'datamaps-subunits');
			var geoData = topojson.feature(data, data.objects.world).features
				.filter(function(feature) {
					return feature.id !== "ATA"; // get rid of Antarctica
				});
			background.selectAll('path.datamaps-subunit')
				.data(geoData)
				.enter()
				.append('path')
				.attr('d', that.path)
				.attr('class', function(d) {
					return 'datamaps-subunit ' + d.id;
				})
				.style('fill', '#BBBBBB')
				.style('stroke-width', 1)
				.style('stroke', '#FDFDFD');
			subunits.selectAll('path.datamaps-subunit')
				.data(geoData)
				.enter()
				.append('path')
				.attr('d', that.path)
				.attr('class', function(d) {
					return 'datamaps-subunit ' + d.id;
				})
				.style('fill', '#BBBBBB')
				.style('stroke-width', 1)
				.style('stroke', '#FDFDFD')
				.on('click', function(d) { opts.clicked(that, d.id, d3.event) });

			if (callback !== undefined) {
				callback(that, error);
			}
		});

		return this;
	}

	/**
	 * Colorize the map by country (wipes all previous colors)
	 * @param  {Object}   data     the map data, in the form of {'country': score}
	 *                             score is 1 (good)-100 (bad); ex. {"USA": 10}, {"JPN": 5}
	 * @param  {Function} callback A function(err) to be called on completion of colorization
	 */
	Map.prototype.colorCountries = function(data, callback) {
		var error = null;

		d3.select("#foreground").selectAll('.datamaps-subunit').style('fill', function(d) {
			if (data.hasOwnProperty(d.id)) {
				return dangerLevelToColor(data[d.id]);
			}
			return '#BBBBBB';
        });

		if (callback !== undefined) {
			callback(error);
		}
	};

	/**
	 * Colorize the map by a graph of danger points (for the zoomed-in country view); (wipes all previous colors)
	 * @param  {Array}   data      the map data, with each entry containing:
	 *                             [{
	 *                             	position: {latitude: 24.4667, longitude: 54.3667},
	 *                             	score: 9, // 1-100
	 *                             	force: 10 // 1-100, how much the color should bleed out from this lat/long
	 *                             }]
	 * @param  {Function} callback A function(err) to be called on completion of colorization
	 */
	Map.prototype.colorPoints = function(data, callback) {
		var that = this;
		var error = null;

		var g = this.svg.select("#pointsLayer");
		var defs = this.svg.append("defs");

		_.each(data, function(d) {
			var lng = d.position.longitude;
			var lat = d.position.latitude;
			var coords = [that.bounds.x + Math.random() * that.bounds.length,
			              that.bounds.y + Math.random() * that.bounds.height];
			//var coords = that.transform(that.projection(latLong));

			var num = Math.floor(Math.random()*10000);
			var grad = defs
				.append("radialGradient")
				.attr("gradientUnits", "objectBoundingBox")
				.attr("id", "grad" + num);
			var color = dangerLevelToColor(d.score);
			grad.append("stop")
				.attr("offset", "0%")
				.attr("stop-color", color)
				.attr("stop-opacity", "100%");
			grad.append("stop")
				.attr("offset", "100%")
				.attr("stop-color", color)
				.attr("stop-opacity", "0%");
			g.append("ellipse")
				.attr("class", "dot")
				.attr("cx", coords[0])
				.attr("cy", coords[1])
				.attr("rx", d.force * that.k / 20)
				.attr("ry", d.force * that.k / 20)
				.style("opacity", "0")
				.style("fill", "url(#grad" + num + ")")
				.transition()
				.duration(500)
				.style("opacity", "1");
		});

		if (callback !== undefined) {
			callback(error);
		}
	};

	/**
	 * Zoom this map in on a specific country
	 * @param  {string}   country  The 3-letter country code (ex. 'USA')
	 * @param  {object}   bounds   The bounding box to contain the country in, in pixels
	 *                             Ex. {x: 10, y: 10, length: 200, height: 100}
	 * @param  {Function} callback A callback to fire once the zooming is complete, callback(err)
	 */
	Map.prototype.zoom = function(country, bounds, callback) {
		var that = this;
		var error = null;
		this.bounds = bounds;

		//d3.selectAll("g#pointsLayer").data([]).exit().remove();
		d3.selectAll(".dot").data([]).exit().remove();
		var g = this.svg.selectAll('.datamaps-subunits');
		var centroid = this.path.centroid(d3.select('.' + country).data()[0]);
		var countryBox = this.path.bounds(d3.select('.' + country).data()[0]);
		var x = centroid[0],
			y = centroid[1],
			countryWidth = countryBox[1][0] - countryBox[0][0],
			countryHeight = countryBox[1][1] - countryBox[0][1];
		var k = Math.min(bounds.length / countryWidth, bounds.height / countryHeight);
		x += ((this.width - bounds.length) / 2 - bounds.x)/ k;

		this.transformStr = "translate(" + this.width / 2 + "," + this.height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")";
		this.k = k;
		this.transform = function(coords) {
			return translate(scale(translate(coords, [-x, -y]), k), [this.width / 2, this.height / 2]);
		};

		g.selectAll("path").classed("active", true);

		g.transition()
			.duration(1000)
			.attr("transform", that.transformStr)
			.each("end", function() {
				if (callback !== undefined) {
					callback(error);
				}
			});
		d3.select("#background").selectAll('.datamaps-subunit')
			.transition()
			.duration(1000)
			.style("opacity", "1");
		d3.select("#foreground").selectAll('.datamaps-subunit')
			.transition()
			.duration(1000)
			.style("opacity", "0");
		d3.selectAll('.' + country)
			.transition()
			.duration(1000)
			.style("opacity", "0.4");

	};

	/**
	 * Zoom this map out to the whole world.
	 * @param  {Function} callback A callback to fire once the zooming is complete, callback(err)
	 */
	Map.prototype.unzoom = function(callback) {
		var error = null;

		d3.selectAll("g#pointsLayer").data([]).exit().remove();
		var g = this.svg.select('.datamaps-subunits');
		var x = this.width / 2;
		var y = this.height / 2;
		var k = 1;

		g.selectAll("path").classed("active", false);

		g.transition()
			.duration(1000)
			.attr("transform", "translate(" + this.width / 2 + "," + this.height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
			.each("end", function() {
				if (callback !== undefined) {
					callback(error);
				}
			});
		console.log("AHH");
		d3.selectAll('.datamaps-subunit')
			.transition()
			.duration(1000)
			.style("opacity", "1");
	};

	return {
		world: Map
	};
});
