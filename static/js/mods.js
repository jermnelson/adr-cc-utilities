function MODSStubViewModel() {
   var self = this;
   self.chosenContentModel = ko.observable();
   self.extentValue = ko.observable();
   self.formValue = ko.observable();
   self.showAlternativeTitle = ko.observable(false);
   self.showContributors = ko.observable(false);
   self.showCorporateCreators = ko.observable(false);
   self.showCorporateContributors = ko.observable(false);
   self.showExtent = ko.observable(false);
   self.showGenre = ko.observable(false);
   self.showForm = ko.observable(false);
   self.showSubjectDates = ko.observable(false);
   self.meetingMinutesTemplate = ko.observable(false);
   self.topicOne = ko.observable();
   self.genreOptions = ko.observableArray();
   self.newsletterTemplate = ko.observable(false);
   self.typeOfResource = ko.observable();

   self.displayContentModel = function() {
     switch(self.chosenContentModel()) {
        // Meeting Minutes
        case "1":
            self.resetForm();
            self.meetingMinutesTemplate(true);
            self.topicOne("Meeting minutes");
            self.showAlternativeTitle(true);
            self.showCorporateCreators(true);
            self.showExtent(true);
            self.typeOfResource("text"); 
            var topic_one = $("#AddTopicBtn").prev(); 
            topic_one.after("<input name=\'subject_topics\' class=\'form-control\' type=\'text\' value=\'Universities and colleges\'></input>");
            break;

        // Newsletter
        case "2":
          self.resetForm();
          self.newsletterTemplate(true);
          self.showAlternativeTitle(true);
          self.showContributors(true);
          self.showGenre(true);
          self.genreOptions.push({ name: "Periodical", value: "periodical" });
          self.genreOptions.push({ name: "Newspaper", value: "newspaper"});
          self.typeOfResource("text"); 

          break;

        // Podcast
        case "3":
          self.resetForm();
          self.showCorporateCreators(true);
          self.showExtent(true);
          self.showForm(true);
          self.showGenre(true);
          self.typeOfResource("sound recording");
          self.extentValue("1 audio file");
          self.formValue("podcast");
          break;

        // Video
        case "4":
          self.resetForm();
          self.showCorporateCreators(true);
          self.showExtent(true);
          self.showForm(true);
          self.showGenre(true);
          self.extentValue("1 video file");
          self.formValue("video clip");
          self.genreOptions.push({ name: "Videorecording", value: "videorecording"}); 
          self.typeOfResource("moving image"); 
          break;

       // Master Form displays everything
       case "5":
          self.resetForm()
          self.showAlternativeTitle(true);
          self.showContributors(true);
          self.showCorporateCreators(true);
          self.showGenre(true);
          self.showExtent(true);
          self.showForm(true);
          self.showSubjectDates(true);
          break;

        default:
          self.resetForm();
    }

   }

   self.addAdditionalField = function(btn_name, name) {
     var last_field = $("#" + btn_name).prev();
     last_field.after("<input name=\'" + name + "\' type=\'text\' class=\'form-control\' maxlength=\'255\'></input>");
   }

   self.addCorporateCreator = function() {
      self.addAdditionalField("AddCorporateCreatorBtn", "corporate_creators");
   }

   self.addCorporateContributor = function() {
     self.addAdditionalField("AddCorporateContributorBtn", "corporate_contributors");
   }

  self.addContributor = function() {
     self.addAdditionalField("AddContributorBtn", "contributors");
   }

   self.addCreator = function() {
    self.addAdditionalField("AddCreatorBtn", "creators");
   }

   self.addDate = function() {
    self.addAdditionalField("AddDateBtn", "subject_dates");
   }

   self.addOrganization = function() {
     self.addAdditionalField("AddOrgBtn", "organizations");
   }

   self.addPerson = function() {
     self.addAdditionalField("AddPersonBtn", "subject_people");
   }

   self.addPlace = function() {
     self.addAdditionalField("AddPlaceBtn", "subject_places");
   }


   self.addTopic = function() {
     self.addAdditionalField("AddTopicBtn", "subject_topics");
   }
   
   self.resetForm = function() {
     self.genreOptions([{ name: "Choose...", value: null}]);
     self.extentValue("");
     self.formValue("");
     self.showExtent(false);
     self.showForm(false);
     self.showGenre(false);
     self.newsletterTemplate(false);
     self.meetingMinutesTemplate(false);
     self.showAlternativeTitle(false);
     self.showContributors(false);
     self.showCorporateCreators(false);
     self.showSubjectDates(false);
     self.topicOne("");
     self.typeOfResource(""); 


   }
 }