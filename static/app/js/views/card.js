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

		initialize: function () {

			// render off the bat
			this.render();
		
		},

		render: function() {
			console.log(this.template(this.model.attributes));
			this.$el.html(this.template(this.model.attributes));
			return this;
		}

	});

	return Card;
});
