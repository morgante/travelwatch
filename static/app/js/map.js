define([
	'jquery',
	'underscore'
], function ($, _) {

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
	function Map($el, data, opts, callback) {
		console.log('I will make a map');
		console.log($el, data, callback);

		this.map = 'I AM A MAP';
		var error = null;

		callback(this, error);
	}

	/**
	 * Colorize the map by country (wipes all previous colors)
	 * @param  {Object}   data     the map data, in the form of {'country': score}
	 *                             score is 1 (good)-100 (bad); ex. {"USA": 10}, {"JPN": 5}
	 * @param  {Function} callback A function(err) to be called on completion of colorization
	 */
	Map.prototype.colorCountries = function(data, callback) {
		var error = null;

		console.log('I am coloring by country', data);

		callback(error);
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

		console.log('I am coloring by the graph', data);

		callback(error);
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

		callback(error);
	};



	return {
		world: Map
	};
});