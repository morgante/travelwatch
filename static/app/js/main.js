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
	}, {}, function(worldMap, error) {
		console.log('this is the map callback', worldMap, error);
	});

	console.log('I am a test');

});