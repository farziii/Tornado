<?php 
/* 	
If you see this text in your browser, PHP is not configured correctly on this hosting provider. 
Contact your hosting provider regarding PHP configuration for your site.

PHP file generated by Adobe Muse CC 2015.0.2.310
*/

require_once('form_process.php');

$form = array(
	'subject' => 'Dashboard Form ارائه',
	'heading' => 'ارائه فرم جدید',
	'success_redirect' => '',
	'resources' => array(
		'checkbox_checked' => 'علامت‌دار',
		'checkbox_unchecked' => 'بی‌علامت',
		'submitted_from' => 'فرم از وب‌سایت زیر دریافت شد: ‎%s',
		'submitted_by' => 'آدرس IP بازدیدکننده: ‎%s',
		'too_many_submissions' => 'اخیراً تعداد موارد ارائه شده از این IP خیلی زیاد بوده است',
		'failed_to_send_email' => 'ارسال ایمیل ناموفق بود',
		'invalid_reCAPTCHA_private_key' => 'کلید خصوصی reCAPTCHA نامعتبر است.',
		'invalid_field_type' => 'قسمت ‎\'%s\'‎ ناشناخته است.‎',
		'invalid_form_config' => 'پیکربندی قسمت \'‎%s\' نامعتبر است.',
		'unknown_method' => 'روش درخواست سرور ناشناخته'
	),
	'email' => array(
		'from' => '',
		'to' => ''
	),
	'fields' => array(
		'Email' => array(
			'order' => 1,
			'type' => 'email',
			'label' => 'لینک وبسایت',
			'required' => true,
			'errors' => array(
				'required' => 'قسمت \'لینک وبسایت\' مورد نیاز است.',
				'format' => 'ایمیل در قسمت \'لینک وبسایت\' نامعتبر است.'
			)
		),
		'custom_U1640' => array(
			'order' => 2,
			'type' => 'string',
			'label' => 'توضیحات',
			'required' => false,
			'errors' => array(
			)
		)
	)
);

process_form($form);
?>
