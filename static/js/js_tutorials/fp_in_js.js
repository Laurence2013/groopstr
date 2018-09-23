var
obj1 = {value: 1},
obj2 = {value: 2},
obj3 = {value: 3};

// var values = [];
// function accumulate(obj) {
//   values.push(obj.value);
// }
// accumulate(obj1);
// accumulate(obj2);
//
// console.log(values);

// function accumulate2(obj) {
//   var values = [];
//   values.push(obj.value);
//   return values;
// }
// console.log(accumulate2(obj1));
// console.log(accumulate2(obj2));
// console.log(accumulate2(obj3));

var ValueAccumulator = function(obj) {
  var values = [];
  var accumulate = function() {
    values.push(obj.value);
  };
  accumulate();
};
// console.dir(ValueAccumulator(obj1)); wont work as undefined will come up, this is because accumulate() method inside of ValueAccumulator doesn't know what obj is
// accumulate = ValueAccumulator(obj1); wont work because accumulate doesn't know what obj is, for this you need closure

var ValueAccumulator2 = function() {
  var values = [];
  var accumulate = function(obj) {
    if (obj) {
      values.push(obj.value);
      return values;
    } else {
      return values;
    }
  };
  return accumulate;
};

var accumulator = ValueAccumulator2();
accumulator(obj1);
accumulator(obj2);
console.log(accumulator());
