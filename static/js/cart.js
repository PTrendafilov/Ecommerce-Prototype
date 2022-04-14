var updateBtns=document.getElementsByClassName('update-cart')

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId=this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId,'action:',action)
        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log("Sending data...")
    
    var url='/update_item/'

    fetch(url,{
        method:'Post',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action': action})
    })
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        window.location = "http://127.0.0.1:8000/product?id="+data;
    })
}


let addBtn=document.getElementById('add-button');

addBtn.addEventListener('click',function(){
    var productId=this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId,'action:',action)
    console.log('USER:', user)
})

