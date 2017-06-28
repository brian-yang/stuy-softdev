var years = ["2008", "2016"];
var years_data = {"2008":
		  [2.55, [2.6 + "_Excise Taxes",4.2 + "_Other Taxes",45.4 + "_Individual Income Taxes",12.1 + "_Corporate Income Taxes",35.7 + "_Payroll Taxes"],
		   3.02, [14.8 + "_Others",34.5 + "_Social Security, Unemployment, and Labor",22.1 + "_Medicare and Health",20.3 + "_National Defense",8.3 + "_Net Interest"],
		   1.87, [13.7 + "_Net Interest",53.6 + "_Social Security, Unemployment, and Labor",33.3 + "_Medicare and Health"]],

		  "2016":
		  [2.99, [2.9 + "_Excise Taxes",6.5 + "_Other Taxes",48.8 + "_Individual Income Taxes",8.8 + "_Corporate Income Taxes",33 + "_Payroll Taxes"],
		   3.54, [14.5 + "_Others",36.4 + "_Social Security, Unemployment, and Labor",28 + "_Medicare and Health",15.1 + "_National Defense",6 + "_Net Interest"],
		   2.44, [10 + "_Net Interest",51.1 + "_Social Security, Unemployment, and Labor",38.9 + "_Medicare and Health"]]
		 };

for (var i = 0; i < years.length; i++) {
    var revenue = d3.select("#revenue_amount_" + years[i]);
    revenue.selectAll("p")
	.data([years_data[years[i]][0]])
        .enter()
        .append("p")
        .text( function(d) {
	    return "$" + d + " trillion";
	});

    var revenue_chart = d3.select("#revenue_" + years[i]);
    revenue_chart.selectAll("div")
	.data(years_data[years[i]][1])
        .enter()
        .append("div")
        .style("width", function(d) {
	    var results = d.split("_");
	    return parseFloat(results[0]) * 25 + "px";
	})
        .text( function(d) {
	    var results = d.split("_");
	    return results[0] + "% " + results[1];
	});

    var spending = d3.select("#spending_amount_" + years[i]);
    spending.selectAll("p")
	.data([years_data[years[i]][2]])
        .enter()
        .append("p")
        .text( function(d) {
	    return "$" + d + " trillion";
	});

    var spending_chart = d3.select("#spending_" + years[i]);
    spending_chart.selectAll("div")
	.data(years_data[years[i]][3])
        .enter()
        .append("div")
        .style("width", function(d) {
	    var results = d.split("_");
	    return parseFloat(results[0]) * 25 + "px";
	})
        .text( function(d) {
	    var results = d.split("_");
	    return results[0] + "% " + results[1];
	});

    var mandatory_spending = d3.select("#mandatory_spending_amount_" + years[i]);
    mandatory_spending.selectAll("p")
	.data([years_data[years[i]][4]])
        .enter()
        .append("p")
        .text( function(d) {
	    return "$" + d + " trillion";
	});

    var mandatory_spending_chart = d3.select("#mandatory_spending_" + years[i]);

    mandatory_spending_chart.selectAll("div")
	.data(years_data[years[i]][5])
        .enter()
        .append("div")
        .style("width", function(d) {
	    var results = d.split("_");
	    return parseFloat(results[0]) * 25 + "px";
	})
        .text( function(d) {
	    var results = d.split("_");
	    return results[0] + "% " + results[1];
	});
}
