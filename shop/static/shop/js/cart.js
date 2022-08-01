var updateBtns = document.getElementsByClassName('update-cart')
//Adding an event handler to each button
for(var i = 0; i < updateBtns.length;i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log("product:",productId,"action:",action)
		console.log('user:',user)
		if (user === 'AnonymousUser') {
			console.log('Not logged in')
		} else {
			updateUserOrder(productId,action)
		}
	})
}
const why=""
function updateUserOrder(productId,action){
	console.log("USer logged in")
	//Url for sending post data
	//var url = '/update_item/'
	fetch('https://dawa-app.herokuapp.com/shop/update_item/',{
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'productId':productId,'action':action})
	})

	.then((response) => {
		return response.json()
	})
	.then((data) => {
		console.log("data:",data)
		location.reload()
	})
}