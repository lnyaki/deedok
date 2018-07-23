// Define a new component called button-counter
console.log("registering button-counter")
console.log(Vue.options.components)
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button class="btn btn-primary" v-on:click="count++">You clicked me <b>{{ count }}</b> times.</button>'
})
