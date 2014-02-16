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
		console.log(query);
		ss = _.map(query, function(s) { return "\"" + s + "\""}).join(' ');
		$.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?fl=_id,web_url,lead_paragraph,abstract,headline,keywords,pub_date,word_count,source,document_type,news_desk&api-key=a23184e7a28923153d114039b3b92b8e:7:68825444", {
			// "query": query,
			"fq": "document_type:(\"article\") AND headline:(" + ss + ")"
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
