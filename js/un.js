function getDayName(date) {
	return date.toLocaleString(undefined, {weekday:'long'});
}

function getMonthName(date) {
	return date.toLocaleString(undefined, {month:'long'});
}


$(function(){
// Create a date
 var d = new Date();
	var today=d;
 // Set to first of month
 d.setDate(1);
 // Create string
 console.log(`The first of ${getMonthName(d)} was a ${getDayName(d)}.`);
	$("#date_range_preselect").val("this_month");
		var todaystr=today.toISOString().split("T")[0]
		var dstr=d.toISOString().split("T")[0]

	$("#date_from").val(d);
	$("#date_to").val(todaystr);
	$("#date_from").change(function(){
	$("#date_range_preselect").val("custom");
	});
	$("#date_to").change(function(){
	$("#date_range_preselect").val("custom");
	});
	$("#date_range_preselect").change(function(){
 var d = new Date();
	var today=d;
 // Set to first of month
 d.setDate(1);
	var yesterday = today;

	//
	yesterday.setDate(yesterday.getDate() - 1);
                var my_date_from=Date.parse(Date.parse(date_from.value)).toDateString();
                var my_date_to=Date.parse(Date.parse(date_to.value)).toDateString();
		var todaystr=today.toISOString().split("T")[0]
		var yesterdaystr=yesterday.toISOString().split("T")[0]
		if (my_date_from === "today"){
		date_from.value=todaystr;
		date_to.value=todaystr;
	}else if (my_date_from === "today"){
		date_from.value=yesterdaystr;
		date_to.value=yesterdaystr;

		}
	});
});
