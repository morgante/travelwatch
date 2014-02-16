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

	String.prototype.capitalize = function() {
	    return this.charAt(0).toUpperCase() + this.slice(1);
	}

	// api.get_nyt("hello sir", function(err, data) {
		// console.log("ny", data);
	// });

	// notifier.notify({
	// 	"title": "This is nonsense",
	// 	"content": "I am a Samson."
	// });



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