define([
	'jquery',
	'underscore',
	'd3',
	'topojson',
], function ($, _, d3, topojson) {

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
		var projection = d3.geo.equirectangular()
			.scale((this.width + 1) / 2 / Math.PI)
			.translate([this.width / 2, this.height / 1.8]);
		this.path = d3.geo.path()
			.projection(projection);

		d3.json("/static/app/world.topo.json", function(error, data) {
			var subunits = that.svg.insert('g', ':first-child')
				.attr('class', 'datamaps-subunits');
			var geoData = topojson.feature(data, data.objects.world).features
				.filter(function(feature) {
					return feature.id !== "ATA"; // get rid of Antarctica
				});
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

		d3.selectAll('.datamaps-subunit').style('fill', function(d) {
			if (data.hasOwnProperty(d.id)) {
				return d3.interpolateRgb('green', 'red')(data[d.id] / 100);
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
	 *                             {
	 *                             	position: {latitude: 24.4667, longitude: 54.3667},
	 *                             	score: 9, // 1-100
	 *                             	force: 10 // 1-100, how much the color should bleed out from this lat/long
	 *                             }
	 * @param  {Function} callback A function(err) to be called on completion of colorization
	 */
	Map.prototype.colorPoints = function(data, callback) {
		var error = null;

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
		var error = null;

		// TODO(zjn): respect bounds
		var g = this.svg.select('g');
		var centroid = this.path.centroid(d3.select('.' + country).data()[0]);
		var x = centroid[0];
		var y = centroid[1];
		var k = 4;

		g.selectAll("path").classed("active", true);

		g.transition()
			.duration(750)
			.attr("transform", "translate(" + this.width / 2 + "," + this.height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
			.style("stroke-width", 1.5 / k + "px")
			.each("end", function() {
				if (callback !== undefined) {
					callback(error);
				}
			});

	};

	/**
	 * Zoom this map out to the whole world.
	 * @param  {Function} callback A callback to fire once the zooming is complete, callback(err)
	 */
	Map.prototype.unzoom = function(callback) {
		var error = null;

		var g = this.svg.select('g');
		var x = this.width / 2;
		var y = this.height / 2;
		var k = 1;

		g.selectAll("path").classed("active", false);

		g.transition()
			.duration(750)
			.attr("transform", "translate(" + this.width / 2 + "," + this.height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
			.style("stroke-width", 1.5 / k + "px")
			.each("end", function() {
				if (callback !== undefined) {
					callback(error);
				}
			});
	};

	return {
		world: Map
	};
});
