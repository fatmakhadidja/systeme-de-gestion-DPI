import { TestBed } from '@angular/core/testing';

import { LaborantinService } from './laborantin.service';

describe('LaborantinService', () => {
  let service: LaborantinService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LaborantinService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
