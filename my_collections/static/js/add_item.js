
var addItem = addItem || {}

addItem.customFieldSeed = 1;

addItem.init = function (){

	$('#save-btn').on('click',addItem.save);

	$('#add-field-btn').on('click',addItem.addCustomField);


}

addItem.save = function(){
	console.log("save");
};

addItem.addCustomField = function(){
	var nameHtml = '<div class="col-lg-5 col-md-5 col-sm-5"><input type="text" required="true" class="form-control" id="label" name="label" placeholder="Field name"></div>';
	var valueHtml = '<div class="col-lg-6 col-md-6 col-sm-6"><input type="text" required="true" class="form-control" id="value" name="value" placeholder="Field value"></div>';
	var removeBtnHtml = '<div class="col-lg-1 col-md-1 col-sm-1 remove-field-btn"><button id="' + addItem.customFieldSeed + '" class="btn btn-danger btn-sm remove-field-btn"><i class="fa fa-times" aria-hidden="true"></i></button></div>'
	var html = '<div id="custom-field'+ addItem.customFieldSeed + '" class="form-group row">' + nameHtml + valueHtml + removeBtnHtml + '</div>';
	$('#custom-fields-div').append(html);	

	$('#' + addItem.customFieldSeed).on('click',function(){
		btnId = this.id;
		addItem.removeCustomField('custom-field' + btnId.toString());
	});

	addItem.customFieldSeed += 1;
};

addItem.removeCustomField = function(id){
	$('#' + id).remove();
}

addItem.init();
