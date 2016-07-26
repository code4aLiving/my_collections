
var addItem = addItem || {}

addItem.customFieldSeed = 1;

addItem.init = function (){

	$('#save-btn').on('click',addItem.save);

	$('#add-field-btn').on('click',addItem.addCustomField);

	$('#save-btn').on('click', addItem.save);
}

addItem.save = function(){
	console.log("save");
};

addItem.addCustomField = function(){
	var nameHtml = `<div class="col-lg-4 col-md-4 col-sm-4">
						<input type="text" required="true" class="form-control custom-label" id="label" name="label" placeholder="Field name">
					</div>`;
	var valueHtml = `<div class="col-lg-4 col-md-4 col-sm-4">
						<input type="text" required="true" class="form-control custom-value" id="value" name="value" placeholder="Field value">
					</div>`;
	var typeHtml = `<div class="col-lg-2 col-md-3 col-sm-3">
						<select class="form-control custom-type">
							<option value="1">Number</option>
	                		<option value="2">Date</option>
	                		<option value="3">Text</option>
	                	</select>                			
	                </div>`;
	var removeBtnHtml = `<div class="col-lg-1 col-md-1 col-sm-1 remove-field-btn">
							<button id="` + addItem.customFieldSeed + `" class="btn btn-danger btn-sm remove-field-btn">
								<i class="fa fa-times" aria-hidden="true"></i>
							</button>
						</div>`;
	var html = '<div id="custom-field'+ addItem.customFieldSeed + '" class="form-group row">' + nameHtml + valueHtml + typeHtml + removeBtnHtml + '</div>';
	$('#custom-fields-div').append(html);	

	$('#' + addItem.customFieldSeed).on('click',function(){
		btnId = this.id;
		addItem.removeCustomField('custom-field' + btnId.toString());
	});

	addItem.customFieldSeed += 1;
};

addItem.removeCustomField = function(id){
	$('#' + id).remove();
};

addItem.save = function(){
	var csrftoken = getCookie('csrftoken');
	data = {    name : $('#name').val(),
			 	description : $('#description').val()
			};
	
	var customLabels = $('.custom-label');
	var customValues = $('.custom-value');
	var customTypes = $('.custom-type')

	for (var i = 0; i<customLabels.length; i++) {
		var type = parseInt($(customTypes[i]).val());
		var value;
		switch(type)
		{
			case 1:
				//Number
				value = parseFloat($(customValues[i]).val());
				break;
			case 2:
				//Date
				value = new Date(Date.parse($(customValues[i]).val()));
				break;
			case 3:
				//Text
				value = $(customValues[i]).val();
				break;
		}
		data[$(customLabels[i]).val()] = value
	}
	postData = {
		csrf_token : csrftoken,
		id : 1,
		data : data
	}
	$.post("add_item",function(postData){
		console.log(data);
	});

	//console.log(data);
};

addItem.init();

//For getting CSRF token
function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
 return cookieValue;
}