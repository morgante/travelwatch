define([
	'jquery',
	'underscore',
    'backbone',
    'map',
    'models/scores',
    'views/dashboard'
], function ($, _, Backbone, Map, Scores, Dashboard) {

	var $map = $('.map');

	// get scores data
	var scores = new Scores();

	console.log('hello sir');

	scores.fetch({
		success: function(collection, response, options) {
			dash = new Dashboard({collection: collection});
		},
		error: function(collection, response, options) {
			alert('Sorry, we are experiencing technical difficulties.');
			console.log(collection, response, options);
		}
	});

});