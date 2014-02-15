define([
	'jquery',
	'underscore',
    'backbone'
], function ($, _, Backbone) {

	// Score Model
	// ---------------
	var Score = Backbone.Model.extend({
		defaults: function() {
			return {
				code: "USA",
				name: "United States of America",
				score: 19 // 1-100
			};
		}
	});

	// Scores Collection
	// ---------------
	var Scores = Backbone.Collection.extend({
		// Reference to this collection's model.
		model: Score,

		url: '/api/scores',

		getObject: function() {
			return _.object(this.pluck('code'), this.pluck('score'));
		}
	});

	// Note that we export the entire collection
	// --- if we need to use the model, we can just use Profiles.model
    return Scores;
});