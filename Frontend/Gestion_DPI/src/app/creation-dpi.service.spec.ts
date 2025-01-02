import { TestBed } from '@angular/core/testing';

import { CreationDpiService } from './creation-dpi.service';

describe('CreationDpiService', () => {
  let service: CreationDpiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreationDpiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
