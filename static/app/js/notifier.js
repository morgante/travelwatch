
define([
	'jquery',
	'underscore',
	'pnotify'
], function ($, _, pnotify) {

	function notify(data) {
		pnotify({
    			title: data.title,
   			text: data.content,
   		        animate_speed: 'fade',
   		        opacity: .8
		});
		console.log('Notification', data.title, data.content);
	}

	return {
		notify: notify
	};
});
