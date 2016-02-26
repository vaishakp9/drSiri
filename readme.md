DOCS

Server for PerkHack Customer Advertorial-Review Incentivisation System

For PerkHack
Host : 192.168.1.22:5421

/resto<br>
Method : GET Request<br>
Header : "uid : johndoe"<br>

This method returns a csv string with all details of the restaurant based on uid, passed as a header


/weight<br>
Method : GET Request<br>
Header : "object_id: johndoe"<br>

This method returns credits based on how popular the post is, ie, number of likes


/getSentiment<br>

Method : GET Request<br>
Header : "text : text_to_be_analysed"<br>

This method returns a value between -1 and 1 that accurately depicts the mood of the text, so that the quality of the post can be evaluated, and appropriate Perk credits can be assigned to the reviewer

/testImg<br>
Method : GET Request<br>
Header : "link : http://link-to-image"<br>

This method processes the image, returns 1 if its a picture with food, 0 if the picture has no food. Used for validating image posted on FB wall to stop spammers