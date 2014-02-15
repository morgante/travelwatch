define([
	'jquery',
	'underscore',
	'd3',
	'topojson',
	'datamaps'
], function ($, _, d3, topojson, Datamap) {
	// TODO(zjn): make colors better

	/**
	 * Makes a world map from given data
	 *
	 *   Maybe see: http://datamaps.github.io/
	 * 
	 * @param  element    $el      jquery reference for container; replace this container's contents with the map
	 * @param  {Object}   options  Object containing options, none currently defined
	 *                    .clicked Callback for when a country is clicked, clicked(country, evt)
	 * @param  {Function} callback A function to be called when the mapping is done, callback(this, error);
	 */
	function Map($el, opts, callback) {
		// TODO(zjn): move this somewhere reasonable
		var hsl2rgb = function(hue, saturation, lightness) {
			var hue2rgb = function(p, q, t) {
				if(t < 0) t += 1;
				if(t > 1) t -= 1;
				if(t < 1/6) return p + (q - p) * 6 * t;
				if(t < 1/2) return q;
				if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
				return p;
			};
			var q;
			if (lightness < 0.5) {
				q = lightness * (1 + saturation);
			} else {
				q = lightness + saturation - lightness * saturation;
			}
			var p = 2 * lightness - q;
			var r = Math.floor(255 * hue2rgb(p, q, hue + 1/3));
			var g = Math.floor(255 * hue2rgb(p, q, hue));
			var b = Math.floor(255 * hue2rgb(p, q, hue - 1/3));
			return ['rgb(', r, ', ', g, ', ', b, ')'].join('');
		};
		var fillColors = { defaultFill: 'purple' };
		_.each(_.range(1, 101), function(dangerLevel) {
			var hue = Math.floor(30 - dangerLevel * (30 / 100)) / 100;
			fillColors[dangerLevel] = hsl2rgb(hue, 0.8, 0.4);
		});
		console.log(fillColors);
		fillColors['defaultFill'] = '#BBB';

		this.map = new Datamap({
			element: $el.get(0),
			done: function(datamap) {
				datamap.svg.selectAll('.datamaps-subunit')
					.on('click', function(country) {
						opts.clicked(country, d3.event);
					});
			},
			fills: fillColors,
		});

		var error = null;

		if (callback !== undefined) {
			callback(this, error);
		}

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

		// TODO(zjn): wipe previous colors
		var fillData = _.object(_.map(data, function(score, country) {
			return [country, { fillKey: score }];
		}));
		this.map.updateChoropleth(fillData);

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

		this.map.bubbles(_.map(data, function(obj) {
			// TODO(zjn): add color to bubbles
			return {
				radius: obj.force,
				latitude: obj.position.latitude,
				longitude: obj.position.longitude
			};
		}));

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

		console.log('I am zooming', country, bounds, callback);

		if (callback !== undefined) {
			callback(error);
		}
	};



	return {
		world: Map
	};
});
