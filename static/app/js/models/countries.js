define([
	'jquery',
	'underscore',
    'backbone'
], function ($, _, Backbone) {

	// Country Model
	// ---------------
	var Country = Backbone.Model.extend({
		idAttribute: "code",

		initialize: function() {
			this.on("change:points", this.normalizePoints, this);
		},

		normalizePoints: function() {
			var points = [];
			var changed = false;

			_.each(this.get("points"), function(point) {
				if (point.force === undefined) {
					changed = true
					point.force = point.score
				}
				points.push(point);
			});

			if (changed) {
				this.set("points", points);
			}
		}
	});

	// Countries Collection
	// ---------------
	var Countries = Backbone.Collection.extend({
		// Reference to this collection's model.
		model: Country,

		url: '/api/countries',

		getOne: function(code, callback) {
			// get country
			var country = this.add({"code": code});
			country.fetch({
				success: function(model) {
					console.log('fetched', model.get('name'));

					callback(null, model);
				}
			});

		}
	});

	// Note that we export the entire collection
	// --- if we need to use the model, we can just use Profiles.model
    return Countries;
});