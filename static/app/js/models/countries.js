define([
	'jquery',
	'underscore',
    'backbone',
    'api'
], function ($, _, Backbone, api) {

	// Country Model
	// ---------------
	var Country = Backbone.Model.extend({
		idAttribute: "code",

		defaults: {
			"entities": [],
			"infos": []
		},

		initialize: function() {
			var self = this;

			this.on("change:points", this.normalizePoints, this);

			this.on("change:entities", this.setInfos, this);

			api.get_advisory(this.get('code'), function(err, data) {
				self.set("advisory", data[0]);

				api.get_entities(self.get("advisory").advisory, function(err, data) {
					var entries = self.set("entities", data.entities);
				});
			});
		},

		setInfos: function() {
			var entities = this.get('entities');
			var infos = [];
			var types = ["NaturalDisaster", "Region", "City"];

			_.each(entities, function(entity) {
				if (_.indexOf(types, entity.type) > -1) {
					if (entity.disambiguated && entity.disambiguated.name) {
						entity.name = entity.disambiguated.name;
					} else {
						entity.name = entity.text;
					}

					infos.push(entity);
				}
			});

			console.log(entities);

			this.set('infos', infos);
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