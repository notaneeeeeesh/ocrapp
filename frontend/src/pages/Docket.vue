<template>
    <div>
        <h1>Docket</h1>
        <div>
            <h1 class="container">Upload Image</h1>
            <div>
                <div class="file-container">
                    <div>
                        <form>
                            <input type="file" id="media" accept="image/png"
                                @change="(event) => handleFileUpload(event)" />
                        </form>
                    </div>
                </div>
                <div>
                    <img v-if="renderImage" :src="renderImage">
                </div>
                <button class="bg-gray-500 rounded-2xl px-5 mt-2" @click="handleSend">Send?</button>
                <button class="bg-gray-500 rounded-2xl px-5 mt-2" @click="printData">Print</button>
                <div>
                    <div v-if="unsavedData" class="flex flex-wrap gap-5">
                        <div v-for="(value, field) in unsavedData" :key="field">
                            <p>{{ field }}</p>
                            <input v-model="unsavedData[field]" type="text" />
                        </div>
                    </div>
                    <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="receiveData"
                        @click="saveEntries">Save?</button>
                    <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="receiveData"
                        @click="handleSubmit">Submit?</button>
                    <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="receiveData"
                        @click="handleClear">Clear?</button>
                    <!-- <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="receiveData" @click="eidResource.fetch()">Fetch?</button> -->
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { fileToBase64, createResource, createListResource } from 'frappe-ui'

const imageData = ref({
    mime: "",
    content: ""
});

const renderImage = ref()

const unsavedData = ref()
const receiveData = ref(
    {
        "fleet": "",
        "reg_no": "",
        "make": "",
        "purpose": "",
        "out_to": "",
        "out_datetime": "",
        "out_kms": "",
        "out_driver": "",
        "in_from": "",
        "in_kms": "",
        "in_datetime": "",
        "in_driver": "",
        "description": "",
        "remarks": ""
    }
)

const handleFileUpload = (e) => {
    var file = e.target.files[0]
    if (!file) return;
    fileToBase64(file).then((data) => {
        data = data.split(",")
        renderImage.value = data
        imageData.value.mime = data[0]
        imageData.value.content = data[1]
    })
};

const handleSend = () => {
    sendImage.submit().then((data) => {
        for (const key in data) {
            receiveData.value[key] = data[key]
        }
        unsavedData.value = receiveData.value
    })
}

const handleSubmit = () => {
    if (!receiveData.value) {
        console.log("empty");
        return
    }
    eidResource.insert.submit(receiveData.value)
    handleClear()
}

const handleClear = () => {
    imageData.value = {
        mime: "",
        content: ""
    };
    renderImage.value = ""
    unsavedData.value = ""
    receiveData.value = {
        "fleet": "",
        "reg_no": "",
        "make": "",
        "purpose": "",
        "out_to": "",
        "out_datetime": "",
        "out_kms": "",
        "out_driver": "",
        "in_from": "",
        "in_kms": "",
        "in_datetime": "",
        "in_driver": "",
        "description": "",
        "remarks": ""
    }
}

const printData = () => {
    console.log("Image Data:")
    console.log(imageData.value)
    console.log("Receive Data:")
    console.log(receiveData.value)
    console.log("Unsaved Data:")
    console.log(unsavedData.value)
}


const sendImage = createResource({
    url: 'ocrapp.api.docket.getDocket',
    params: {
        str: imageData.value
    }
})

const saveEntries = () => {
    receiveData.value = unsavedData.value
    console.log("Saved!")
}

const eidResource = createListResource({
    doctype: "Docket",
    fields: ["*"],
    auto: true
})

</script>
