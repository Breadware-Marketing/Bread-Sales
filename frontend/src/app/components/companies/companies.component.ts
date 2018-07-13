import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

import { CompaniesService } from '../../services/companies.service';
import { Company } from '../../models/company';

import { Angular2Csv } from 'angular2-csv/Angular2-csv';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  // Component properties
  allCompanies: Company[];
  statusCode: number;
  requestProcessing = false;
  companyIdToUpdate = null;
  processValidation = false;

  // Create Form
  companyForm = new FormGroup({
    name: new FormControl('', Validators.required),
    industry: new FormControl('', Validators.required)
  });

  constructor(private companyService: CompaniesService) {}

  ngOnInit(): void {
    this.getAllCompanies();
  }

  // Fetch all Companies
  getAllCompanies() {
    this.companyService
      .getAllCompanies()
      .subscribe(
        data => (this.allCompanies = data),
        errorCode => (this.statusCode = errorCode)
      );
  }

  downloadAll() {
    const options = {
      fieldSeparator: ',',
      quoteStrings: '"',
      decimalseparator: '.',
      showLabels: true,
      showTitle: false,
      useBom: true
    };

    console.log(this.allCompanies);
    // tslint:disable-next-line:no-unused-expression
    new Angular2Csv(this.allCompanies, 'All Companies', options);
  }

  // Handle create and update article
  onCompanyFormSubmit() {
    this.processValidation = true;
    if (this.companyForm.invalid) {
      return; // Validation failed, exit from method.
    }

    // Form is valid, now perform create or update
    this.preProcessConfigurations();
    const company = this.companyForm.value;
    if (this.companyIdToUpdate === null) {
      // Generate company id then create company
      this.companyService.getAllCompanies().subscribe(companies => {
        // Generate Company ID
        const maxIndex = companies.length - 1;
        const companyWithMaxIndex = companies[maxIndex];
        const companyId = companyWithMaxIndex.id + 1;
        company.id = companyId;

        // Create Company
        this.companyService.createCompany(company).subscribe(successCode => {
          this.statusCode = successCode;
          this.getAllCompanies();
          this.backToCreateCompany();
        }, errorCode => (this.statusCode = errorCode));
      });
    } else {
      // Handle Company Update
      company.id = this.companyIdToUpdate;
      this.companyService.updateCompany(company).subscribe(successCode => {
        this.statusCode = successCode;
        this.getAllCompanies();
        this.backToCreateCompany();
      }, errorCode => (this.statusCode = errorCode));
    }
  }

  deleteCompany(companyId: string) {
    this.preProcessConfigurations();
    this.companyService.deleteCompanyById(companyId).subscribe(successCode => {
      // this.statusCode = successCode;
      // Expecting success code 204 from server
      this.statusCode = 204;
      this.getAllCompanies();
      // this.backToCreateArticle();
    }, errorCode => (this.statusCode = errorCode));
  }

  getLead(companyId: string){
    console.log(companyId);
  }

  // Perform preliminary processing configurations
  preProcessConfigurations() {
    this.statusCode = null;
    this.requestProcessing = true;
  }

  // Go back from update to create
  backToCreateCompany() {
    this.companyIdToUpdate = null;
    this.companyForm.reset();
    this.processValidation = false;
  }
}
