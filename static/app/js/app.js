require.config({
	baseUrl: "static/app/js",
	paths: {
		"jquery": "//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min",
		"underscore": "../../components/underscore/underscore",
		"backbone": "../../components/backbone/backbone",
	},
	shim: {
		'jquery': {
             exports: '$'
         },
		'underscore': {
			exports: '_'
		},
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone'
		}
	}
});

// Load the main app module to start the app
require(["main"]);