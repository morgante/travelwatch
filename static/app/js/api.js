define([
	'jquery',
	'underscore',
], function ($, _) {

	function get_advisory(code, callback) {
		$.get("/api/alerts/" + code, function(data) {
			callback(null, data)
		}, "json");
	}

	return {
		get_advisory: get_advisory
	};
});
