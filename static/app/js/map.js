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
	 * @param  {Object}   data     the map data, in the form of {'country': score}
	 *                             score is 1-10; ex. {"USA": 1}, {"JPN": 2}
	 * @param  {Object}   options  Object containing options, none currently defined
	 *                    .clicked Callback for when a country is clicked, clicked(country, evt)
	 * @param  {Function} callback A function to be called when the mapping is done, callback(this, error);
	 */
	function mapWorld($el, data, opts, callback) {
		console.log('I will make a map');
		console.log($el, data, callback);

		this.map = 'I AM A MAP';
		var error = null;

		callback(this, error);
	}

	return {
		world: mapWorld
	};
});