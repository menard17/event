<template>
  <div class="row">
    <div class="col-lg-6">
      <input type="text" v-model="title" class="form-control mt-2" placeholder="Title">
      <input type="date" v-model="BirthDate" class="form-control mt-2" placeholder="BirthDate">
      <input type="time" v-model="time" class="form-control mt-2" placeholder="BirthDate">
      <button @click="postEvent" class="btn btn-block btn-success">Save</button>
    </div>
    <div class="col-lg-6">
      <table class="table">
        <thead>
          <th>Name</th>
          <th>Start</th>
          <th>End</th>
        </thead>
        <tbody>
          <tr v-for="event in events" v-bind:key="event.name">
            <td>{{event.event_name}}</td>
            <td>{{event.event_name}}</td>
            <td>{{event.event_name}}</td>
          </tr>
          <td>
            <buttton @click="getOne(event)" class="btn bn-sm btn-success"><i class="fa fa-pencil"></i></buttton>
            <buttton @click="deleteOne(event)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></buttton>
          </td>
        </tbody>
      </table>
    </div>
    {{events}}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      events: null,
      event_name: '',
      event_start: '',
      event_end: '',
    }
  },

  mounted() {
    this.getAll();
  },
  methods:{
    getAll() {
      axios.get(`event/get-all-event`)
          .then((res) => {
            console.log("text", res.data)
            this.events = res.data
          })
    },
    getOne(event) {
      this.event_name = event.event_name
      this.event_start = event.event_start
      this.event_end = event.event_end
    },
    deleteOne(url) {
      axios.delete(url, {auth:{
        usernam: 'juliebuan',
        password: 'password123'
        }})
    },
    postEvent(){
      axios.post(`http://localhost:8000/event`,
          {auth:{
              usernam: 'juliebuan',
              password: 'password123'
            }},
          {name:this.event_name, event_start: this.event_start, event_end: this.event_end }
          )
    }
  }
}
</script>

<style scoped>
</style>
