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

	function get_nyt(query, callback) {
		$.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:(%22World%22)%20AND%20document_type:(%22article%22)&fl=_id,web_url,lead_paragraph,abstract,headline,keywords,pub_date,word_count,source,document_type,news_desk&api-key=a23184e7a28923153d114039b3b92b8e:7:68825444", {
			"query": query
		}, function(data) {
			try {
				callback(null, data.response.docs);
			} catch(e) {
				callback(e, []);
			}
		}, "json");
	}

	return {
		get_advisory: get_advisory,
		get_entities: get_entities,
		get_nyt: get_nyt
	};
});
