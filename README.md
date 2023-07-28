# FREE Tradingview Automated Trader 
made by: Storm-07 <br />

  I came up with a way to brute force automate trades on tradingview without signing up for a membership using macros and webhooks.
There are a few services you may need to sign up for first if you don't already have accounts but do not worry because these are also free unless you'd like to make more than 50 trades per day. 

Service #1: Tradingview
  This one is fairly self explanatory as it is the platform we will be using to make trades. IMPORTANT NOTE: For this automated trader, you must have a dedicated computer open for as long as you intend to make trades for. This computer will be the only one allowed to have a tradingview window open because free accounts are only allowed to have one window open at a time.

Service #2: Visual Studio Code
  You will very likely have to have this code editor installed in order to edit your macros unless you share the same type of PC as me. Do not worry if you are not experienced with programming, a simple google search or youtube video will help with any issues setting up your macro.

Service #3: Pipedream.com
  Ignoring the name, this site will act as the webhook that receives tradingview email alerts and sends a trigger to your server in order to activate the buying and selling macros.

Service #4: ngrok
  This is another free pipeline service that will allow the pipedream webhook to connect with your flask server.

Service #5: AutoHotKey
  You might not actually have to sign up for this but this will be the language(?) that we use to setup the macros. If you are not familiar with macros, they are simply a string of user inputs that execute different operations. For example we could set shift + G to left click on the corner of your screen.

# STEPS FOR SETTING UP AUTOMATION
1. Download Visual Studio Code, Download AutoHotKey, Download ngrok
2. Create a new workflow in pipedream using an email as the trigger, then add a step called "Send any HTTP Request" then change the "GET" type request to "POST", ignore the URL for now as we will create that later, then go into headers and add a header name of "content-type" and add the corresponding header type to "application/json". Then in the body section set the content type to "application/json" and change the key to "plain-text-body" and the value to "{{steps.trigger.event.body.text}}". What all this does is access the email we will receive from out tradingview email alert and extract the word either "buy" or "sell" in order to send to the server.
3. Go into your profile settings in tradingview, in the privacy settings change the SMS email to the random email generated by the pipedream trigger in the first step of your workflow. it should looks something like: "[randomchars]@upload.pipedream.net". So when tradingview receives an alert from an indicator or strategy (as long as it says either "buy" or "sell" in the alert instructions) the alert will trigger your workflow.
4. Make sure that you have an indicator setup in tradingview that is able to trigger alerts that issue "buy" and "sell" signals
5. download the folder from this github repo and open it in visual studio code. This contains the server that receives the pipedream trigger, and the macros that will buy and sell assets in the market.
6. All you need to change in these files are the paths labeled in BuyActivator.py, SellActivator.py and Receiver.py. Also you will need to create your own macro as I do not have the same monitor resolution as you. For now the macros are set to display windows saying either "Buy!" or "Sell!" if they are successfully triggered
7. (!) you will need to repeat this step whenever you restart the autotrader. Open your ngrok terminal and type "ngrok http 5000". This will open a pipeline on port 5000 that will connect your server to the pipedream workflow. If you see a timer of some kind saying the pipeline will expire, this means you need to complete a few more steps in your ngrok account. I believe it is just authentication of your account, a tutorial should be on their site. Once you have completed setting up your account, you will be able to have this pipeline open indefinitely which is exactly what we want for automated trading. Copy the FORWARDING URL generated from ngrok and paste it into the webhook section of your workflow in pipedream. after you have the forwarding URL pasted, make sure to add '/webhook' to the end of the URL. This is what your flask server will be looking for to connect the webhook trigger.
8. test that your workflow functions correctly by either letting your tradingview alert trigger, or send an email to the pipedream generated email that contains the words "buy" or "sell" somewhere in the body of the email (those two words are case sensitive).
9. Setup your macros, unfortunately, this process can be a bit difficult but most of your macro will look like this: "Click, 100 200" where 100 and 200 represent coordinates on your screen, If all you do is click buttons and enter amounts in tradingview to execute a trade, here is the documentation from autohotkey to setup your macro: https://www.autohotkey.com/docs/v1/lib/MouseClick.htm & https://www.autohotkey.com/docs/v1/lib/Send.htm <br /> I highly recommend testing your macros with actual button shortcuts before you try and use them with the automated trader and then delete the buttons after your macros are done, you will need to delete the .exe files from the folder and compile your macros to move the new .exe files back into the folder. The python files need both the .ahk and .exe files to run the macro.
10. If your workflow in pipedream successfully runs, you are now ready to start running the auto trader!

# Running the AutoTrader
(Only start the autotrader after a short entry)
1. Run Receiver.py in Visual Studio Code on the computer you wish to have open
2. Open ngrok and type "ngrok http 5000" (without the quotations)
3. copy and paste forwarding URL into webhook in pipedream task and append /webhook to the end of the URL
4. test and deploy pipedream workflow
5. open tradingview window to how your macro was setup and make sure your indicator is active and sends buy/sell alerts

As mentioned before, pipedream only permits 100 inputs a day which is 50 trades so keep this in mind.
Enjoy and good luck trading!
