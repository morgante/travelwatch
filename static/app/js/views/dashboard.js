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
			this.$card = $('#card', this.$el);

			this.$card.hide();

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
			
			// this.openCountry('USA');
		
		},

		closeCountry: function(code) {
			var view = this;

			view.map.unzoom();

			view.card.$el.fadeOut();

		},

		openCountry: function(code) {
			var view = this;

			if (view.country != undefined && view.country.get("code") == code) {
				view.map.unzoom();
			}

			view.map.zoom(code, {x: 50, y: 50, length: 400, height: 400}, function() {
				console.log('I finished zooming')
			view.countries.getOne(code, function(err, country) {
				view.country = country;

				view.map.colorPoints(country.get("points"));

				view.card = new Card({
					el: $('#card', view.$el),
					model: country,
					dashboard: view
				});

				view.$card.fadeIn();
				
			});
			});

		},

		render: function () {
			var view = this;

			var zoomed;
			this.map = new Map.world(this.$map, {
				clicked: function(map, country, evt) {
					view.openCountry(country);

					// if (!zoomed || zoomed != country) {
					// 	map.zoom(country,
					// 		{x: 50, y: 50, length: 400, height: 400},
					// 		function() {
					// 			map.colorPoints([{
					// 				position: {latitude: 24.4667, longitude: 54.3667},
					// 				score: 20,
					// 				force: 10
					// 			}, {
					// 				position: {latitude: 23.4667, longitude: 55.3667},
					// 				score: 30,
					// 				force: 10
					// 			}, {
					// 				position: {latitude: 23.4667, longitude: 53.3667},
					// 				score: 40,
					// 				force: 50
					// 			}]);
					// 		});
					// 	zoomed = country;
					// } else {
					// 	map.unzoom();
					// }
				}
			}, function(map, error) {
				view.map = map;

				console.log('this is the map callback', map, error);

				map.colorCountries(view.collection.getObject(), function(err) {
					console.log('Countries have been colored');

					setTimeout(function() {
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
