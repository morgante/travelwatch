define([
	'jquery',
	'underscore',
    'backbone',
    'map',
    'models/countries',
    'views/card'
], function ($, _, Backbone, Map, Countries, Card) {
	// The Dashboard View
	// ---------------

	var Dashboard = Backbone.View.extend({

		el: '#dashboard',

		initialize: function () {
			this.$map = $('.map', this.$el);

			this.scores = this.collection;
			this.countries = new Countries;

			// render off the bat
			this.render();

			// // this.listenTo(app.todos, 'reset', this.refresh);
			// this.listenTo(profiles, 'add', this.setMatch);

			// // console.log( Profiles );

			// profiles.add({
			// 	'name': 'Samantha Xu'
			// });
			// 
			
			this.openCard('USA');
		
		},

		openCard: function(countryCode) {
			var view = this;

			this.countries.getOne(countryCode, function(err, country) {
				console.log('I have a country', country);

				view.card = new Card({
					el: $('#card', view.$el),
					model: country
				});
				
			});
		},

		render: function () {
			var view = this;

			console.log('I am magic mike');

			var zoomed;
			this.map = new Map.world(this.$map, {
				clicked: function(map, country, evt) {
					if (!zoomed || zoomed != country) {
						map.zoom(country,
							{x: 50, y: 50, length: 400, height: 400});
						zoomed = country;
					} else {
						map.unzoom();
					}
				}
			}, function(map, error) {
				view.map = map;

				console.log('this is the map callback', map, error);

				map.colorCountries(view.collection.getObject(), function(err) {
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

				});
		},

		// setMatch: function (profile) {			
		// 	var view = new Match({ model: profile });
		// 	$('#quick-match').html(view.render().el);

		// 	// console.log( view );
		// },

	});

	return Dashboard;
});
