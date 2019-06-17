function nextDay (year, month, day) {
    bigMonths = [1, 3, 5, 7, 8, 10, 12];
    smallMonths = [2, 4, 6, 9, 11];

    for (let i=0; i <= bigMonths.length; i++) {
        let longMonth = bigMonths[i];    
        if (longMonth == month && day == 31) {
            if (month == 12) {
                month = 01;
                year += 1;
            }
            day = 01;
        }
    for (let j=0; j <= smallMonths.length; j++) {
        let shortMonth = smallMonths[j];
        if (shortMonth == month && (day == 30 || day == 28)) {
            month += 1;
            day = 01;
        }
    }
    }
    return year + "-" + month + "-" + day
}

// Better solution

function calcNextDay(year, month, day)  {
    let date = new Date(year, month-1, day);
    let oneDay = 24 * 60 * 60 * 1000; // milliseconds in 1 day
    let nextDate = new Date(date.getTime() + oneDay);
    return nextDate.getFullYear() + "-" +
      (nextDate.getMonth() + 1) + '-' +
      nextDate.getDate();
  }