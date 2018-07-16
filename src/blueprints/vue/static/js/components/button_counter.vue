// Define a new component called button-counter
console.log("registering button-counter")
console.log(Vue.options.components)
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
