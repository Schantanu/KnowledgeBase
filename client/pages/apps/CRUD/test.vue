<template>
  <div class="container">
    <br />

    <div class="control">
      <a class="button is-info" @click="isAddModalActive = true">
        <span class="is-size-6">+ Add Item</span>
      </a>
    </div>

    <b-modal :active.sync="isAddModalActive" :width="600" scroll="keep">
      <form @submit.prevent="validateBeforeSubmit">
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Add Item</p>
          </header>

          <section class="modal-card-body">
            <b-field
              label="Delivery"
              :type="{'is-danger': errors.has('delivery')}"
              :message="errors.first('delivery')"
            >
              <div class="field has-addons is-expanded">
                <div class="control is-expanded">
                  <!-- <input class="input" type="search" placeholder="Enter Delivery Number" v-model="item.delivery"> -->
                  <b-input v-model="item.delivery" name="delivery" v-validate="'required'" />
                </div>
                <div class="control">
                  <a class="button is-info" @click.prevent="searchItems()">Search</a>
                </div>
              </div>
            </b-field>

            <!-- <b-field grouped>
              <b-field label="Customer" expanded>
                <b-input expanded disabled loading></b-input>
              </b-field>
              <b-field label="Delivery Date" expanded>
                <b-input expanded disabled loading></b-input>
              </b-field>
            </b-field>-->

            <b-field label="Detail">
              <b-input type="textarea" v-model="item.detail"></b-input>
            </b-field>
          </section>

          <footer class="modal-card-foot">
            <div class="field is-grouped is-grouped-right">
              <!-- <button type="button" class="button is-info" @click="postItem(), isAddModalActive = false">Submit</button> -->
              <button type="submit" class="button is-primary">Submit</button>
              <button type="button" class="button" @click="isAddModalActive = false">Cancel</button>
            </div>
          </footer>
        </div>
      </form>
    </b-modal>

    <section class="container">
      <form @submit.prevent="validateBeforeSubmit">
        <b-field
          label="First name"
          :type="{'is-danger': errors.has('firstname')}"
          :message="errors.first('firstname')"
        >
          <b-input v-model="firstname" name="firstname" v-validate="'required'" />
        </b-field>

        <b-field
          label="Last name"
          :type="{'is-danger': errors.has('lastname')}"
          :message="errors.first('lastname')"
        >
          <b-input v-model="lastname" name="lastname" v-validate="'required'" />
        </b-field>

        <b-field
          label="Age"
          :type="{'is-danger': errors.has('age')}"
          :message="errors.first('age')"
        >
          <b-input
            type="number"
            v-model="age"
            name="age"
            v-validate="'required|integer|between:18,65'"
          />
        </b-field>

        <b-field
          label="Gender"
          :addons="false"
          :type="{'is-danger': errors.has('gender')}"
          :message="errors.first('gender')"
        >
          <b-radio v-model="gender" name="gender" native-value="M" v-validate="'required'">Male</b-radio>
          <b-radio v-model="gender" name="gender" native-value="F" v-validate="'required'">Female</b-radio>
        </b-field>

        <b-field
          label="Username"
          :type="{'is-danger': errors.has('username')}"
          :message="errors.first('username')"
        >
          <b-input type="text" v-model="username" name="username" v-validate="'required|alpha'" />
        </b-field>

        <b-field
          label="Password"
          :type="{'is-danger': errors.has('password')}"
          :message="errors.first('password')"
        >
          <b-input
            type="password"
            v-model="password"
            name="password"
            v-validate="'required|min:8'"
          />
        </b-field>

        <b-field
          label="Confirm password"
          :type="{'is-danger': errors.has('confirm-password')}"
          :message="[{
                    'The confirm password field is required' : errors.firstByRule('confirm-password', 'required'),
                    'The confirm password is not valid' : errors.firstByRule('confirm-password', 'is')
                }]"
        >
          <b-input
            type="password"
            v-model="confirmPassword"
            name="confirm-password"
            v-validate="{ required: true, is: password }"
          />
        </b-field>

        <b-field
          label="Where did you find us ?"
          :type="{'is-danger': errors.has('question')}"
          :message="errors.first('question')"
        >
          <b-select
            v-model="question"
            name="question"
            placeholder="Select an option"
            v-validate="'required'"
          >
            <option value="google">Google</option>
            <option value="github">Github</option>
            <option value="other">Other</option>
          </b-select>
        </b-field>

        <b-field
          label
          :type="{'is-danger': errors.has('flag-terms')}"
          :message="{'Please check this box to proceed' : errors.firstByRule('flag-terms', 'required')}"
        >
          <b-checkbox
            v-model="flagTerms"
            name="flag-terms"
            v-validate="'required:false'"
          >I agree to the terms and conditions</b-checkbox>
        </b-field>

        <button type="submit" class="button is-primary">Submit</button>
      </form>
    </section>
  </div>
</template>

<script>
import Vue from "vue";
import VeeValidate from "vee-validate";

Vue.use(VeeValidate, {
  events: ""
});

export default {
  data() {
    return {
      isAddModalActive: false,

      item: {
        delivery: "",
        issue_category: "",
        issue: "",
        detail: ""
      },

      firstname: null,
      lastname: null,
      age: null,
      username: null,
      password: null,
      confirmPassword: null,
      gender: null,
      question: null,
      flagTerms: false
    };
  },
  methods: {
    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.$toast.open({
            message: "Form is valid!",
            type: "is-success",
            position: "is-bottom"
          });
          return;
        }
        this.$toast.open({
          message: "Form is not valid! Please check the fields.",
          type: "is-danger",
          position: "is-bottom"
        });
      });
    }
  }
};
</script>