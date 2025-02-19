# Alpaca Auto Trading with Algo10.com

## Overview
This is a basic auto trading program using Alpaca.  It uses buy signals from Algo10.com (which does require a paid subscription).  The intent is to use the signals to buy at the beginning of the day (ex. at or near the opening bell), sets stop losses, and sells at the market close. 

## Prerequisites
 - Setup Alpaca account.  Note: Start with a paper trading account.  This is free of charge.
 - Start with a list of your favorite stocks.  But before trading real money, it is best to sign up for a service to provide indicators of which stocks will go up the next day. This may require a paid subscription, but with many services you can cancel after 30 days of auto trading is not for you.

## Installation
Clone this repo to C: drive

Install Alpaca 
```
pip install alpaca-py
```

Ensure environmental variables are setup on your local machine.  Alpaca provides good examples and how to info: https://github.com/alpacahq/alpaca-trade-api-python

## Set Schedules
Update "run_alpaca.bat" and "run_alpaca_liquidate.bat" to include proper paths

Schedule "run_alpaca.bat" and "run_alpaca_liquidate.bat" in your task scheduler (I use Windows Task Scheduler) which the user will have to setup manually.  
1. Create a daily M-F Windows Task to run "run_aplaca.bat" to buy the assets at the time of the opening bell or shortly after(ex. 8:30AM CT).  This batch file also sets stop losses.
2. Create a daily M-F Windows Task to run "run_aplaca_liquidate.bat" to sell the assets just a few minutes prior to close (ex. 3PM CT).


## About Algo10
Visit https://algo10.com/how-it-works.html to learn more. 


## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
