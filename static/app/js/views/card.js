define([
	'jquery',
	'underscore',
    'backbone',
], function ($, _, Backbone) {
	// The Card View
	// ---------------

	var Card = Backbone.View.extend({
		// Cache the template function for a single item.
		template: _.template($('#card-template').html()),

		"events": {
			'click [data-dismiss="card"]': "close"
		},

		initialize: function(options) {
			_.extend(this, _.pick(options, 'dashboard'));

			this.render();
		},

		close: function() {
			this.dashboard.closeCountry();
		},

		render: function() {
			// console.log(this.template(this.model.attributes));
			this.$el.html(this.template(this.model.attributes));
			return this;
		}

	});

	return Card;
});
