export {};

declare global {
  namespace Express {
    interface Locals {
      validatedReqData: any;
      retrivedDbData: any;

    }
  }
}
