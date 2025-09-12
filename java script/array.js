// const arr=["python",2,3,3,5,6,7,8,9]
//  console.log(arr[)
// for(let i=0;i<arr.length;i++){
//     console.log(arr[i])
// }
// arr.reverse()
// console.log(arr)


// const numbers=[2,3,4,5,690,7,8]
// numbers.sort
// console.log(numbers)
// console.log(numbers.pop())
// console.log(numbers)

// console.log(numbers.push(67))
// console.log(numbers)

// console.log(numbers.unshift(0))
// console.log(numbers)
// array methods and objet methods 


// const num=[1,2,3,4,5,6,7,8,9,0];
// num.unshift(10)
// console.log(num)

// num=[22,3,23,41,55,32,54];
// console.log(num.length);
// console.log(num.pop());
// console.log(num);

// new_arr=num.slice(0,4);
// console.log(new_arr);
// console.log(new_arr.sort((a,b)=>a-b));
// console.log(new_arr.reverse())

// let a=["a","e","j","b","h"];
// console.log(a.sort());
// console.log(a.reverse());

// a.push("g");
// console.log(a);

// a.unshift('hey');
// console.log(a);

// a.splice(1,3,'abcd')
// console.log(a)

// a.shift()
// console.log(a)


// const numbers=[2,4,7,9]
// let squares=numbers.map(num=>num*2)
// console.log(squares)


const numbers=[4,5,7,9,4,8,10]
let  squares=numbers.map(num=>num%2==0)
// let  squares=numbers.filter(num=>num%2==0)
console.log(squares)


// const numbers=[1,2,3,4,5,6,7,8,9]
//  // let A=numbers.reduce((a,b)=>a+b,"")
//  let A=numbers.reduce((a,b)=>a*b,1)

// console.log(A)


numbers.forEach(function Square(num){
  console.log(num*num)  
})
                           

