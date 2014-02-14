define([
	'jquery',
	'underscore',
    'backbone',
    'map',
], function ($, _, Backbone, map) {

	var $map = $('.map');

	map.world($map, {
		"USA": 1,
		"JPN": 3
	}, {
		clicked: function(country, evt) {
			console.log('This county was clicked', country);
		}
	}, function(worldMap, error) {
		console.log('this is the map callback', worldMap, error);
	});

	console.log('I am a test');

});