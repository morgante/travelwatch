define([
	'jquery',
	'underscore'
], function ($, _) {

	function notify(data) {
		console.log('Notification', data.title, data.content);
	}

	return {
		notify: notify
	};
});
