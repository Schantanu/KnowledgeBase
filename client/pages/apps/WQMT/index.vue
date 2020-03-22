<template>
  <div class="container">
    <section class="section">
      <div class="columns">
        <div class="column">
          <div class="is-left">
            <h1 class="title is-4">Delivery App</h1>
            <h2 class="subtitle is-6">To monitor the quality of Deliveries</h2>
          </div>
        </div>

        <div class="column">
          <p class="buttons is-right">
            <a class="button" @click="refreshData()">
              <span class="icon is-small">
                <b-tooltip label="Refresh Data" position="is-top">
                  <b-icon
                    pack="mdi"
                    icon="refresh"
                    size="is-small"
                    custom-size="mdi-24px"
                    type="is-dark"
                  ></b-icon>
                </b-tooltip>
              </span>
            </a>
            <a class="button">
              <span class="icon is-small">
                <b-tooltip label="Export to Excel" position="is-top">
                  <b-icon
                    pack="mdi"
                    icon="file-excel"
                    size="is-small"
                    custom-size="mdi-24px"
                    type="is-dark"
                  ></b-icon>
                </b-tooltip>
              </span>
            </a>
            <a class="button" @click="isInfoModalActive = true">
              <span class="icon is-small">
                <b-tooltip label="Info" position="is-top">
                  <b-icon
                    pack="mdi"
                    icon="help-circle-outline"
                    size="is-small"
                    custom-size="mdi-24px"
                    type="is-dark"
                  ></b-icon>
                </b-tooltip>
              </span>
            </a>
          </p>
        </div>
      </div>
    </section>

    <b-tabs>
      <b-tab-item label="Data" icon="table-large">
        <br />

        <b-field grouped>
          <div class="control">
            <a class="button is-info" @click="clearModal(), isAddModalActive = true">
              <span class="is-size-6">+ Add Item</span>
            </a>
          </div>

          <div class="field has-addons is-expanded">
            <div class="control is-expanded">
              <input class="input" type="search" placeholder="Search Items" v-model="searchTerm" />
            </div>

            <div class="control">
              <a class="button is-info" @click.prevent="searchItems()">Search</a>
            </div>
          </div>
        </b-field>

        <br />

        <b-table
          :data="items"
          :narrowed="true"
          :bordered="true"
          :striped="true"
          :mobile-cards="false"
          :per-page="30"
          :loading="isTableLoading"
          default-sort-direction="desc"
          default-sort="updated_at"
          ref="table"
          paginated
          :opened-detailed="defaultOpenedDetails"
          detailed
          detail-key="pk"
          @details-open="(row, index) => $toast.open({ message: `Expanded ${row.delivery}`, duration: 1000, position: 'is-top', type: 'is-info' })"
          :show-detail-icon="showDetailIcon"
        >
          <template slot-scope="props">
            <b-table-column
              field="delivery"
              label="Delivery"
              width="100"
              numeric
              sortable
            >{{ props.row.delivery }}</b-table-column>

            <b-table-column
              field="issue_category"
              label="Issue Category"
              width="150"
              numeric
              sortable
            >{{ props.row.issue_category }}</b-table-column>
            <b-table-column field="issue" width="200" label="Issue">{{ props.row.issue }}</b-table-column>
            <b-table-column field="detail" label="Detail">{{ props.row.detail }}</b-table-column>
            <b-table-column
              field="updated_at"
              label="Update Date"
              width="170"
              sortable
            >{{ new Date(props.row.updated_at).toLocaleString() }}</b-table-column>
          </template>

          <template slot="detail" slot-scope="props">
            <!-- <div class="content"> -->
            <div>
              <b-field grouped>
                <b-field label="Delivery">
                  <p>{{ props.row.delivery }}</p>
                </b-field>

                <b-field label="Update Date">
                  <p>{{ new Date(props.row.updated_at).toLocaleString() }}</p>
                </b-field>

                <b-field label="Issue Category">
                  <p>{{ props.row.issue_category }}</p>
                </b-field>

                <b-field label="Issue Detail">
                  <p>{{ props.row.issue }}</p>
                </b-field>

                <b-field label="Detail">
                  <p>{{ props.row.detail }}</p>
                </b-field>
              </b-field>

              <br />

              <div class="buttons is-right">
                <button
                  class="button is-warning"
                  @click="fetchItem(props.row.pk), isEditModalActive = true"
                >Edit</button>
              </div>
            </div>
          </template>
        </b-table>
      </b-tab-item>

      <b-tab-item label="Chart" icon="chart-line">
        <iframe
          src="https://public.tableau.com/views/NCAABasketballSalaries/NCAABasketballSalaries?:showVizHome=no&:embed=true"
          height="100%"
          width="100%"
          style="overflow:hidden; overflow-x:hidden; overflow-y:hidden; height=100;"
        ></iframe>
      </b-tab-item>
    </b-tabs>

    <script type="text/javascript"></script>

    <!-- Info Modal -->
    <b-modal :active.sync="isInfoModalActive" :width="600" scroll="keep">
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Info</p>
          </header>
          <section class="modal-card-body">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
              labore et dolore magna aliqua. Sed vulputate mi sit amet mauris commodo quis imperdiet massa.
              Enim nulla aliquet porttitor lacus luctus accumsan tortor. Sapien pellentesque habitant morbi
              tristique senectus et. Viverra orci sagittis eu volutpat odio facilisis. Magna fringilla urna
              porttitor rhoncus dolor. Sed arcu non odio euismod lacinia at quis risus. Libero nunc consequat
              interdum varius.
            </p>
            <br />
            <p>
              Tempor orci dapibus ultrices in iaculis. Nulla porttitor massa id neque aliquam
              vestibulum. Pulvinar etiam non quam lacus suspendisse. Euismod quis viverra nibh cras pulvinar
              mattis. Magna fringilla urna porttitor rhoncus. Duis ut diam quam nulla porttitor massa id neque
              aliquam. Arcu non sodales neque sodales ut etiam sit. Etiam erat velit scelerisque in dictum non
              consectetur a. Mauris a diam maecenas sed enim ut sem viverra.
            </p>
          </section>
          <footer class="modal-card-foot">
            <!-- <button class="button is-success">Save changes</button>
            <button class="button">Cancel</button>-->
          </footer>
        </div>
      </form>
    </b-modal>

    <!-- Add Item Modal -->
    <b-modal :active.sync="isAddModalActive" :width="600" scroll="keep">
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Add Item</p>
          </header>

          <section class="modal-card-body">
            <b-field label="Delivery">
              <div class="field has-addons is-expanded">
                <div class="control is-expanded">
                  <input
                    class="input"
                    type="search"
                    placeholder="Enter Delivery Number"
                    v-model="item.delivery"
                  />
                </div>
                <div class="control">
                  <a class="button is-info" @click.prevent="searchItems()">Search</a>
                </div>
              </div>
            </b-field>

            <div class="columns">
              <div class="column">
                <b-field label="Issue Category" expanded>
                  <b-select v-model="item.issue_category" expanded required>
                    <option value>Select an Issue Category</option>
                    <option
                      v-for="(item, index) in issueList"
                      :key="(item, index)"
                      :value="index"
                    >{{ index }}</option>
                  </b-select>
                </b-field>
              </div>
              <div class="column">
                <b-field label="Issue Detail" expanded>
                  <b-select
                    :disabled="isDisabled"
                    v-model="item.issue"
                    placeholder="Select an Issue Detail"
                    expanded
                    :required="false"
                  >
                    <option value>Select an Issue Detail</option>
                    <option
                      v-for="option in issueList[item.issue_category]"
                      :value="option.value"
                    >{{ option.value }}</option>
                  </b-select>
                </b-field>
              </div>
            </div>

            <b-field label="Detail">
              <b-input type="textarea" v-model="item.detail"></b-input>
            </b-field>
          </section>

          <footer class="modal-card-foot">
            <div class="field is-grouped is-grouped-right">
              <button
                type="button"
                class="button is-info"
                @click="postItem(), isAddModalActive = false"
              >Save</button>
              <button type="button" class="button" @click="isAddModalActive = false">Cancel</button>
            </div>
          </footer>
        </div>
      </form>
    </b-modal>

    <b-modal :active.sync="isEditModalActive" :width="600" scroll="keep">
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Edit Item</p>
          </header>

          <section class="modal-card-body">
            <b-field label="Delivery">
              <div class="field has-addons is-expanded">
                <div class="control is-expanded">
                  <input
                    class="input"
                    type="search"
                    placeholder="Enter Delivery Number"
                    v-model="item.delivery"
                  />
                </div>
                <div class="control">
                  <a class="button is-info" @click.prevent="searchItems()">Search</a>
                </div>
              </div>
            </b-field>

            <div class="columns">
              <div class="column">
                <b-field label="Issue Category" expanded>
                  <b-select
                    v-model="item.issue_category"
                    placeholder="Select an Issue Category"
                    expanded
                    required
                  >
                    <option v-for="(item, index) in issueList">{{ index }}</option>
                  </b-select>
                </b-field>
              </div>
              <div class="column">
                <b-field label="Issue Detail" expanded>
                  <b-select
                    :disabled="isDisabled"
                    v-model="item.issue"
                    v-if="item.issue_category"
                    placeholder="Select an Issue Detail"
                    expanded
                    :required="item.issueCategory == 'Other (Enter Detail)' ? true : false"
                  >
                    <option v-for="option in issueList[item.issue_category]">{{ option.value }}</option>
                  </b-select>
                </b-field>
              </div>
            </div>

            <b-field label="Detail">
              <b-input type="textarea" v-model="item.detail"></b-input>
            </b-field>
          </section>

          <footer class="modal-card-foot">
            <div class="field is-grouped-right">
              <button
                type="button"
                class="button is-info"
                @click="updateItem(), isEditModalActive = false"
              >Save</button>
              <button type="button" class="button" @click="isEditModalActive = false">Cancel</button>
              <button
                type="button"
                class="button is-danger"
                @click="deleteItem(item.pk), isEditModalActive = false"
              >Delete</button>
            </div>
          </footer>
        </div>
      </form>
    </b-modal>

    <b-modal :active.sync="isDeleteModalActive" :width="300">
      <section class="modal-card-body">
        <p>Test</p>
      </section>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Frame",
  head() {
    return {
      title: "WQMT"
    };
  },
  data() {
    return {
      item: [],
      items: [],
      itemID: null,

      isInfoModalActive: false,
      isAddModalActive: false,
      isEditModalActive: false,
      isEdit1ModalActive: false,
      isDeleteModalActive: false,
      defaultOpenedDetails: [1],
      showDetailIcon: true,
      hasMobileCards: false,
      isTableLoading: false,

      // isDisabled: true,

      searchTerm: [],
      item: {
        delivery: "",
        issue_category: "",
        issue: "",
        detail: ""
      },

      issueList: {
        "Packing Slip": [
          { value: "Incorrect Data" },
          { value: "Missing" },
          { value: "Printed on Double Sided Paper" },
          { value: "Serial Number Missing" },
          { value: "Serial Number Incorrect" },
          { value: "Other (Enter Detail)" }
        ],
        Placard: [
          { value: "Incorrect Data" },
          { value: "Missing" },
          { value: "Other (Enter Detail)" }
        ],
        Damage: [
          { value: "Damaged Packaging" },
          { value: "Improperly Packaged" },
          { value: "Other (Enter Detail)" }
        ],
        "Other (Enter Detail)": [{ value: "" }]
      },
      issueDetails: [],
      selectedIssueCategory: "",
      selectedissueDetail: ""
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let items = await $axios.$get("/wqmt/");
      return { items };
    } catch (e) {
      return { items: [] };
    }
  },
  methods: {
    clearModal() {
      (this.item.delivery = this.item.detail = ""),
        (this.item.issue_category = ""),
        (this.item.issue = "");
    },
    refreshData() {
      try {
        this.defaultOpenedDetails = [0];
        this.getData();
        this.$snackbar.open({
          duration: 2000,
          message: "Table refreshed",
          type: "is-light",
          actionText: "Ok"
        });
      } catch (e) {
        this.$snackbar.open({
          duration: 2000,
          message: "Table not refreshed",
          type: "is-danger",
          actionText: "Ok"
        });
      }
    },
    toggle(row) {
      this.$refs.table.toggleDetails(row);
    },

    // API methods
    async getData() {
      try {
        let items = await this.$axios.$get("/wqmt/");

        this.items = items;
      } catch (e) {
        this.items = [];
      }
    },
    async fetchItem(params) {
      const item = await this.$axios.$get(`/wqmt/${params}`);
      this.item = item;
    },
    async postItem() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      var issueFormData = new FormData();
      for (let data in this.item) {
        issueFormData.append(data, this.item[data]);
      }
      try {
        let response = await this.$axios.$post("/wqmt/", issueFormData, config);
        this.getData();
        this.$snackbar.open({
          duration: 3000,
          message: `Added Issue for Delivery ${this.item.delivery}`,
          type: "is-light",
          actionText: "Ok"
        });
        this.clearModal();
      } catch (e) {
        console.log(e);
      }
    },
    async updateItem() {
      let editedItem = this.item;
      console.log(editedItem.pk);
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let itemFormData = new FormData();
      for (let data in editedItem) {
        itemFormData.append(data, editedItem[data]);
      }
      try {
        let response = await this.$axios.$put(
          `/wqmt/${editedItem.pk}/`,
          itemFormData,
          config
        );
        this.defaultOpenedDetails = [0];
        this.getData();
        this.$snackbar.open({
          duration: 3000,
          message: `Updated Issue for Delivery ${editedItem.delivery}`,
          type: "is-light",
          actionText: "Ok"
        });
      } catch (e) {
        console.log(e);
      }
    },
    async deleteItem() {
      let deletedItem = this.item;
      try {
        let response = await this.$axios.$delete(`/wqmt/${deletedItem.pk}/`);
        this.$snackbar.open({
          duration: 3000,
          message: `Deleted Issue for Delivery ${deletedItem.delivery}`,
          type: "is-light",
          actionText: "Ok"
        });
        this.getData();
      } catch (e) {
        console.log(e);
      }
    }
  },
  computed: {
    isDisabled: function() {
      if (
        this.item.issue_category.length == 0 ||
        this.item.issue_category == "Other (Enter Detail)"
      ) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>

<style>
td {
  max-width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.content {
  white-space: normal;
}

.content p:not(:last-child) {
  margin-bottom: 0;
}
</style>
