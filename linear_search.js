var array = [12,34,1,4,3,2,10,13];

linear_search =>(arr,key) {
  for(var i=0;i<arr.length-1;i++){
    if(arr[i] === key){
      return i;
    }
  }
  return -1;
};

console.log(linear_search(array,4));
console.log(linear_search(array,44));
