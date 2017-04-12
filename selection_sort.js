var array = [12,34,36,46];
var count = 0;


function selection_sort(list){

  for(var i=0;i<list.length-1;i++){
    var smallestIndex = list.length-1;
    for(var j=i;j<list.length-1;j++)
      count++;
      if (list[j] < list[smallestIndex]){
        smallestIndex = j;
      }
      var temp = list[smallestIndex];
      list[smallestIndex] = list[i];
      list[i] = temp;
  }
  console.log("count: ",count);
  return list;

}

console.log(selection_sort(array));
