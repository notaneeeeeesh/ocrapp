<template>
  <div>
    <h1>Hello</h1>
    <div>
      <h1 class="container">Image Upload Vue.js</h1>
      <div>
        <div class="file-container">
          <div>
            <form>
              <input type="file" id="media" accept="image/png" @change="(event) => handleFileUpload(event)" />
            </form>
          </div>
        </div>
        <div>
          <img v-if="renderImage" :src="renderImage">
        </div>
        <button class="bg-gray-500 rounded-2xl px-5" @click="handleSend">Send?</button>
        <button class="bg-gray-500 rounded-2xl px-5" @click="printData">Print</button>
        <div>
          <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="receiveData" @click="saveEntries">Save?</button>
          <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="receiveData" @click="handleSubmit">Submit?</button>
          <div class="grid" v-if="unsavedData" v-for="(value, field, index) in unsavedData" :key="field">
            {{ index }}  {{ field }}
            <input v-model="unsavedData[field]" type="text"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { fileToBase64, createResource } from 'frappe-ui'

const sentData = ref({  
  mime: "",
  content: ""
});

const renderImage=ref("")

const unsavedData = ref({})
const receiveData = ref({})

const handleFileUpload = (e) => {
  var file = e.target.files[0]
  if (!file) return;
  fileToBase64(file).then((data) => {
    data = data.split(",")
    renderImage.value = data
    sentData.value.mime=data[0]
    sentData.value.content=data[1]
  })
};

const handleSend = () => { 
  sendRequest.submit().then((data) => {
    receiveData.value = data
    unsavedData.value = receiveData.value
  })
}

const handleSubmit = () => {
  makeDoc.submit().then(() => console.log("sent!"))
}

const printData = () => {
  console.log("sentData")
  console.log(sentData.value)
  console.log("Receive Data:")
  console.log(receiveData.value )
  console.log("Unsaved Data:")
  console.log(unsavedData.value )
}

const makeDoc = createResource({
  url: 'ocrapp.api.makeEid.makeDoc',
  params: {
    str: receiveData.value
  }
})

const sendRequest = createResource({
  url: 'ocrapp.api.eid.getEid',
  params: {
    str: sentData.value
  }
})

const saveEntries = () => {
  // receiveData.value = unsavedData.value
  console.log("Saved!")
}



</script>
