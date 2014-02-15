define([
	'jquery',
	'underscore',
    'backbone'
], function ($, _, Backbone) {

	// Country Model
	// ---------------
	var Country = Backbone.Model.extend({
		idAttribute: "code"
	});

	// Countries Collection
	// ---------------
	var Countries = Backbone.Collection.extend({
		// Reference to this collection's model.
		model: Country,

		url: '/mock/countries',

		getOne: function(code, callback) {
			// get country
			var country = this.add({"code": "USA"});
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