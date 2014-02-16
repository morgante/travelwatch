define([
	'jquery',
	'underscore',
], function ($, _) {

	function get_advisory(code, callback) {
		$.get("/api/alerts/" + code, function(data) {
			callback(null, data)
		}, "json");
	}

	function get_entities(text, callback) {
		$.get("/api/alchemy/text/TextGetRankedNamedEntities", {
			"text": text
		}, function(data) {
			callback(null, data)
		}, "json");
	}

	return {
		get_advisory: get_advisory,
		get_entities: get_entities
	};
});
