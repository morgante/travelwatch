define([
	'jquery',
	'underscore',
    'backbone',
    'map',
], function ($, _, Backbone, Map) {

	var $map = $('.map');

	Map.world($map, {
		clicked: function(country, evt) {
			console.log('This county was clicked', country);
		}
	}, function(map, error) {
		console.log('this is the map callback', worldMap, error);

		map.colorCountries({
			"USA": 1,
			"JPN": 3
		}, function(err) {
			console.log('Countries have been colored');

			setTimeout(function() {
				map.colorPoints([{
					position: {latitude: 24.4667, longitude: 54.3667},
					score: 20,
					force: 10
				}], function(err) {
					console.log('new coloring applied');
				});
			}, 1000);
		});

		map.zoom('USA', {x: 10, y: 10, length: 100, height: 200});
	});

	console.log('I am a test');

});