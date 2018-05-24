import { TestBed, inject } from '@angular/core/testing';

import { CompaniesService } from './companies.service';

describe('CompaniesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CompaniesService]
    });
  });

  it('should be created', inject([CompaniesService], (service: CompaniesService) => {
    expect(service).toBeTruthy();
  }));
});
