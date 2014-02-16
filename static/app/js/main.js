define([
	'jquery',
	'underscore',
    'backbone',
    'map',
    'api',
    'notifier',
    'models/scores',
    'views/dashboard'
], function ($, _, Backbone, Map, api, notifier, Scores, Dashboard) {

	var $map = $('.map');

	// get scores data
	var scores = new Scores();

	notifier.notify({
		"title": "This is nonsense",
		"content": "I am a Samson."
	});

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