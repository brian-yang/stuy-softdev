// the previously commented out calendar javascript
// is in calendar.js.old

// =======================================
// DATE VARIABLE
// =======================================
var d = new Date();

// =======================================
// FUNCTIONS
// =======================================
function getMonthName(month) {
    var monthName = "";
    switch(month){
    case 0:
	monthName = "January";
	break;
    case 1:
	monthName = "February";
	break;
    case 2:
	monthName = "March";
	break;
    case 3:
	monthName = "April";
	break;
    case 4:
	monthName = "May";
	break;
    case 5:
	monthName = "June";
	break;
    case 6:
	monthName = "July";
	break;
    case 7:
	monthName = "August";
	break;
    case 8:
	monthName = "September";
	break;
    case 9:
	monthName = "October";
	break;
    case 10:
	monthName = "November";
	break;
    case 11:
	monthName = "December";
	break;
    }
    return monthName;
}

function weekdays() {
    var dayTags = "<li>Su</li>\n" +
	"<li>Mo</li>\n" +
	"<li>Tu</li>\n" +
	"<li>We</li>\n" +
	"<li>Th</li>\n" +
	"<li>Fr</li>\n" +
        "<li>Sa</li>\n"
    return dayTags;
}

function numDays(year, month) {
    var numTags = "";
    var firstDay = new Date(year, month, 1);
    var daysInMonth = new Date(year, month + 1, 0).getDate();
    // getDay() returns 0 if the day is Sunday, so we make sure that
    // we do not prepend a placeholder if the day is Sunday
    // Otherwise, there would be an extra <li> prepended, messing up
    // the layout of the calendar
    dayNum = firstDay.getDay();
    // redList = weekends(dayNum, daysInMonth);
    if (dayNum != 0) {
	for(i = 0; i < dayNum; i++) {
	    numTags += "<li></li>\n";
	}
    }
    for (i = 1; i <= daysInMonth; i++) {
    	if (dayNum == 0 || dayNum == 6) {
	    numTags += "<li class='closed'>" + i.toString() + "</li>\n "
	} else {
	    numTags += "<li>" + i.toString() + "</li>\n "
	}
	dayNum++;

	if (dayNum == 7) {
	    numTags += "<br/>";
	    dayNum = 0;
	}
    }
    return numTags;
}

function displayDays(year, month) {
    $('.weekdays').append(weekdays());
    $('.days').append(numDays(year, month));
}

function manageDates(date, month, year) {
    // var daysInMonth = new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate();

    $('.days li').each(function(){
	if( month < 10) {
            d1 = new Date(year, month, $(this).text());
            //console.log(d1);
            //console.log($(this).text() + " " + d1.getDay());
            if (d1.getDay() != 0 && d1.getDay() != 6) { 
		$(this).html('<a class="open" href=' + "0" + month.toString() + "-" +
			     $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
            }
	}
	else {
            d1 = new Date(year, month, $(this).text());
            //console.log(d1);
            //console.log($(this).text() + " " + d1.getDay());
            if (d1.getDay() != 0 && d1.getDay() != 6) { 
		$(this).html('<a class="open" href=' + month.toString() + "-" +
			     $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
            }
	}
	
	if ($(this).text() == d.getDate() && month === d.getMonth() && month < 10) {
            d1 = new Date(year, month, $(this).text());
            //console.log(d1);
            //console.log($(this).text() + " " + d1.getDay());
            if (d1.getDay() != 0 && d1.getDay() != 6) { 
		console.log("ugh");
		$(this).html('<span class = "active"> <a href=' + "0" + month.toString() + "-" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
            }   
	}

	if ($(this).text() == d.getDate() && month === d.getMonth() && month >= 10) {
            console.log("hi");
            d1 = new Date(year, month, $(this).text());
            //console.log(d1);
            //console.log($(this).text() + " " + d1.getDay());
            if (d1.getDay() != 0 && d1.getDay() != 6) { 
		$(this).html('<span class = "active"> <a href=' + month.toString() + "-" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
            }
	}

    });
}


// =======================================
// ON DOCUMENT READY
// =======================================

$(document).ready(function(){
    var monthNum = parseInt(d.getMonth());
    var currentYear = parseInt(d.getFullYear());
    var currentDate = parseInt(d.getDate());
    var currentMonth = getMonthName(monthNum);
    $('.m').html(currentMonth);
    $('.y').html(currentYear);
    displayDays(currentYear, monthNum);
    manageDates(currentDate, monthNum, currentYear);

    $(".prev").on("click", function(){
    	console.log("what");
    	$('.weekdays').empty();
    	$('.days').empty();
    	monthNum -= 1;
    	if (monthNum == -1) {
    	    monthNum = 11;
    	    currentYear -= 1;
    	}
    	displayDays(currentYear, monthNum);
    	manageDates(currentDate, monthNum, currentYear);
    	currentMonth = getMonthName(monthNum);
    	$('.m').html(currentMonth);
    	$('.y').html(currentYear);
    });

    $(".next").on("click", function() {
    	$('.weekdays').empty();
    	$('.days').empty();
    	monthNum += 1;
    	if (monthNum == 12) {
    	    monthNum = 0;
    	    currentYear += 1;
    	}
    	displayDays(currentYear, monthNum);
    	manageDates(currentDate, monthNum, currentYear);
    	currentMonth = getMonthName(monthNum);
    	$('.m').html(currentMonth);
    	$('.y').html(currentYear);
    });
});
